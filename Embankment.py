# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__
def bankment(ID,L,h1,i1,H,L0,d0,Density1,Density2,AK,AN,RF,C,FA,PA,VKB,VNB,AUR,AK2,AN2,RF2,C2,FA2,PA2,VKB2,VNB2,AUR2,load1,stress2,stress22):
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import optimization
    import step
    import interaction
    import load
    import mesh
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    import numpy as np
    import math  # 导入math模块

    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
        sheetSize=200.0)
    # 构建模型
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ConstructionLine(point1=(0.0, 25.0), point2=(0.0, -17.5))
    s.VerticalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(-1*(L/2+i1*h1), 0.0), point2=(-1*L/2, h1))
    s.Line(point1=(-1*L/2, h1), point2=(L/2, h1))
    s.Line(point1=(L/2, h1), point2=(L/2+i1*h1, 0.0))
    s.Line(point1=(L/2+i1*h1, 0.0), point2=(L0/2, 0.0))
    s.Line(point1=(L0/2, 0.0), point2=(L0/2, -1*H))
    s.Line(point1=(L0/2, -1*H), point2=(-1*L0/2, -1*H))
    s.Line(point1=(-1*L0/2, -1*H), point2=(-1*L0/2, 0.0))
    s.Line(point1=(-1*L0/2, 0.0), point2=(-1*(L/2+i1*h1), 0.0))
    # 左右对称
    s.SymmetryConstraint(entity1=g[3], entity2=g[5], symmetryAxis=g[2])
    s.SymmetryConstraint(entity1=g[10], entity2=g[6], symmetryAxis=g[2])
    s.SymmetryConstraint(entity1=g[9], entity2=g[7], symmetryAxis=g[2])
    mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['Part-1'].BaseShell(sketch=mdb.models['Model-1'].sketches['__profile__'])
    del mdb.models['Model-1'].sketches['__profile__']
    # 定义路堤集合
    mdb.models['Model-1'].parts['Part-1'].Set(faces=
        mdb.models['Model-1'].parts['Part-1'].faces.findAt(((L/2, h1,0),)), name='all')
    mdb.models['Model-1'].parts['Part-1'].PartitionFaceByShortestPath(faces=mdb.models['Model-1'].parts['Part-1'].faces.
                                                        findAt(((1*L/2, h1,0),)),point1 =(-1*L0/2,0,0), point2 =(L0/2, 0, 0))
    mdb.models['Model-1'].parts['Part-1'].Set(faces=
        mdb.models['Model-1'].parts['Part-1'].faces.findAt(((1*L/2, h1,0),)), name='Set-1')

    # 定义集合
    mdb.models['Model-1'].parts['Part-1'].Set(faces=
        mdb.models['Model-1'].parts['Part-1'].faces.findAt(((-1*L0/2, -1*H,0),)), name='Set-2')
    # 剖分/定义集合
    j=int(math.ceil(h1/d0))
    for i in range(1,j,1):
        mdb.models['Model-1'].parts['Part-1'].PartitionFaceByShortestPath(faces=mdb.models['Model-1'].parts['Part-1'].faces.
                                                    findAt(((L/2, h1,0),)),point1 =(-1*L0/2,i*d0,0), point2 =(L0/2, i*d0,0))
        # nam = 'Set-'+ bytes(i)

        mdb.models['Model-1'].parts['Part-1'].Set(faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(((0, i*d0, 0),)),
                                                  name='fill'+str(int(i)))

    mdb.models['Model-1'].parts['Part-1'].Set(faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(((0, h1, 0),)),
                                                  name='fill'+str(j))
    # 定义材料
    mdb.models['Model-1'].Material(name='embankment')
    mdb.models['Model-1'].materials['embankment'].Density(table=((Density1, ), ))
    mdb.models['Model-1'].materials['embankment'].UserMaterial(
        mechanicalConstants=(AK,AN,RF,C,FA,PA,VKB,VNB,AUR))
    mdb.models['Model-1'].materials['embankment'].Depvar(n=3)

    mdb.models['Model-1'].Material(name='soil')
    mdb.models['Model-1'].materials['soil'].Density(table=((Density2, ), ))
    mdb.models['Model-1'].materials['soil'].UserMaterial(
        mechanicalConstants=(AK2,AN2,RF2,C2,FA2,PA2,VKB2,VNB2,AUR2))
    mdb.models['Model-1'].materials['soil'].Depvar(n=3)
    # 创建截面，赋予材料属性
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', material='embankment', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', material='embankment', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-2', material='soil', thickness=None)
    p = mdb.models['Model-1'].parts['Part-1']
    region = p.sets['Set-1']
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['Part-1']
    region = p.sets['Set-2']
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    # 装配
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='Part-1-1',
        part=mdb.models['Model-1'].parts['Part-1'])
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=OFF, name='Part-1-1',
        part=mdb.models['Model-1'].parts['Part-1'])
    # 定义分析步
    mdb.models['Model-1'].StaticStep(name='fill0', previous='Initial', maxNumInc=100000, initialInc=1, minInc=1e-15)
    mdb.models['Model-1'].StaticStep(name='fill0', previous='Initial',maxNumInc=100000, initialInc=1, minInc=1e-15)
    #生死单元
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Part-1-1'].sets['Set-1']
    mdb.models['Model-1'].ModelChange(name='Int-1', createStepName='fill0',
                                      region=region, activeInStep=False, includeStrain=False)
    # 施加荷载
    mdb.models['Model-1'].Gravity(name='Load-1', createStepName='fill0', comp2=-1 * load1, distributionType=UNIFORM,
                                  field='')
    # 边界条件
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-1 * L0 / 2, -1, 0),))
    a.Set(edges=edges1, name='boundry1')
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((-1, -H, 0),))
    a.Set(edges=edges1, name='boundry2')
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['Part-1-1'].edges
    edges1 = e1.findAt(((L0 / 2, -1, 0),))
    a.Set(edges=edges1, name='boundry3')
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['boundry1']
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial',
                                         region=region, u1=SET, u2=SET, ur3=SET, amplitude=UNSET,
                                         distributionType=UNIFORM, fieldName='', localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['boundry2']
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial',
                                         region=region, u1=SET, u2=SET, ur3=SET, amplitude=UNSET,
                                         distributionType=UNIFORM, fieldName='', localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['boundry3']
    mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Initial',
                                         region=region, u1=SET, u2=SET, ur3=SET, amplitude=UNSET,
                                         distributionType=UNIFORM, fieldName='', localCsys=None)
    # 网格划分
    a = mdb.models['Model-1'].rootAssembly
    partInstances = (a.instances['Part-1-1'],)
    a.seedPartInstance(regions=partInstances, size=0.5, deviationFactor=0.1,
                       minSizeFactor=0.1)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    pickedRegions = f1
    a.setMeshControls(regions=pickedRegions, elemShape=QUAD)
    elemType1 = mesh.ElemType(elemCode=CPE4, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    faces1 = f1
    pickedRegions = (faces1,)
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    a = mdb.models['Model-1'].rootAssembly
    partInstances = (a.instances['Part-1-1'],)
    a.generateMesh(regions=partInstances)
    # 创建job
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.models['Model-1'].keywordBlock.replace(43+2*j, """
** ----------------------------------------------------------------
**
*INITIAL CONDITIONS,TYPE=SOLUTION
part-1-1.Set-1,0.0,"""+str(stress2)+""",0.0
part-1-1.Set-2,0.0,"""+str(stress22)+""",0.0
** STEP: fill0
**""")

    # 创建job
    mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
    mdb.Job(name='Job-'+str(ID), model='Model-1', description='', type=ANALYSIS,
            atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
            memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
            modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
            userSubroutine='D:\\temp\\duncan-chang(1).for', scratch='',
            resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,numGPUs=0)
    mdb.jobs['Job-'+str(ID)].submit(consistencyChecking=OFF)
    mdb.jobs['Job-'+str(ID)].waitForCompletion()

    j = int(math.ceil(h1 / d0))
    for i in range(1, j + 1, 1):
        mdb.models['Model-1'].StaticStep(name='fill' + str(i), previous='fill' + str(i - 1),   maxNumInc=1000000,
                                 stabilizationMagnitude=1.0,
                                 stabilizationMethod=DAMPING_FACTOR, continueDampingFactors=False,
                                 adaptiveDampingRatio=0.05, initialInc=0.01,
                                 solutionTechnique=QUASI_NEWTON)
    # 生死单元
    for i in range(1, j + 1, 1):
        a = mdb.models['Model-1'].rootAssembly
        region = a.instances['Part-1-1'].sets['fill' + str(i)]
        mdb.models['Model-1'].ModelChange(name='Int-' + str(i + 1), createStepName='fill' + str(i),
                                          region=region, activeInStep=True, includeStrain=False)

    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
        predefinedFields=ON, interactions=OFF, constraints=OFF,
        engineeringFeatures=OFF)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Part-1-1'].sets['Set-1']
    mdb.models['Model-1'].Stress(name='Predefined Field-1',
        distributionType=FROM_FILE, fileName='D:/temp/Job-'+str(ID)+'.odb',
        step=1, increment=1)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='geo-'+str(ID), model='Model-1', description='', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF,
        userSubroutine='D:\\temp\\duncan-chang(1).for', scratch='',
        resultsFormat=ODB, multiprocessingMode=DEFAULT,  numCpus=1,numGPUs=0)
    mdb.jobs['geo-'+str(ID)].submit(consistencyChecking=OFF)

    mdb.jobs['geo-' + str(ID)].waitForCompletion()
    print('ok')
    mdb.saveAs(pathName='D:/temp/settlement' + str(ID))

