---
title: "Create a Part"
project: ""
interface: ""
member: ""
kind: "topic"
source: "emodeltoolkit/GettingStarted/Create_a_Part.htm"
---

# Create a Part

See Also

You will typically follow these steps to create a part using the eModelToolkit.

1. Create an application using [eDApplication::Create](../eDApplication/eDApplication_Class.htm).
2. Create a scene ([eDScene](../eDScene/eDScene_Class.htm)) using [eDApplication::CreateScene](../eDApplication/eDApplication_Class.htm).
3. Create and add a new configuration ([eDConfiguration](../eDConfiguration/eDConfiguration_Class.htm)) to that scene using [eDScene::CreateConfiguration](../eDScene/eDScene_Class.htm).
4. Create and add a new part ([eDPart](../eDPart/eDPart_Class.htm)) to that configuration using [eDConfiguration::CreatePart](../eDConfiguration/eDConfiguration_Class.htm).
5. Create a new body ([eDBody](../eDBody/eDBody_Class.htm)) and populate it with data using [eDScene::CreateBody](../eDScene/eDScene_Class.htm) and eDBody methods.

NOTE: [eDCurveList](../eDCurveList/eDCurveList_Class.htm), [eDShellList](../eDShellList/eDShellList_Class.htm), and [eDMarkerList](../eDMarkerList/eDMarkerList_Class.htm) are all independent. In this toolkit, you do not bound curves with marker points or bound faces with curves. Shells may or may not combine to form recognizable surfaces or solid bodies.

1. [eDBody::CreateCurveList](../eDBody/eDBody_Class.htm) //Create sketch segment
2. [eDBody::CreateShellList](../eDBody/eDBody_Class.htm)

[eDShellList::InsertFacets](../eDShellList/eDShellList_Class.htm) //Input face geometry data

1. [eDBody::CreateMarkerList](../eDBody/eDBody_Class.htm)

[eDMarkerList::InsertMarker](../eDMarkerList/eDMarkerList_Class.htm) //Input point data

1. Add the body to the part with [eDPart::AddBody](../eDPart/eDPart_Class.htm).
2. Repeat Steps 3 - 6 to add additional configurations.
3. Create the serialization object ([eDSerializer](../eDSerializer/eDSerializer_Class.htm)) using [eDScene::CreateSerializer](../eDScene/eDScene_Class.htm).
4. Save the scene to disk using [eDSerializer::Serialize](../eDSerializer/eDSerializer_Class.htm) with [eDSerializerParams](../eDSerializerParams/eDSerializerParams_Class.htm) as a parameter.
