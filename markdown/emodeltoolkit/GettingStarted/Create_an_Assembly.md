---
title: "Create an Assembly"
project: ""
interface: ""
member: ""
kind: "topic"
source: "emodeltoolkit/GettingStarted/Create_an_Assembly.htm"
---

# Create an Assembly

See Also

You will typically follow these steps to create an assembly using the eModelToolkit.

1. Create an application using [eDApplication::Create](../eDApplication/eDApplication_Class.htm).
2. Create a scene ([eDScene](../eDScene/eDScene_Class.htm)) using [eDApplication::CreateScene](../eDApplication/eDApplication_Class.htm).
3. Create and add a new configuration ([eDConfiguration](../eDConfiguration/eDConfiguration_Class.htm)) to that scene using [eDScene::CreateConfiguration](../eDScene/eDScene_Class.htm).
4. Create and add a new assembly ([eDAssembly](../eDAssembly/eDAssembly_Class.htm)) to that configuration using [eDConfiguration::CreateAssembly](../eDConfiguration/eDConfiguration_Class.htm). This is the top-level root component.
5. To create a new component with no children:
6. To create a subassembly, create a new assembly ([eDAssembly](../eDAssembly/eDAssembly_Class.htm)) using [eDAssembly::CreateSubAssembly](../eDAssembly/eDAssembly_Class.htm). The parent-child link is created for you.

Add parts or more subassemblies to that assembly using [eDAssembly::CreatePart](../eDAssembly/eDAssembly_Class.htm) and [eDAssembly::CreateAssembly](../eDAssembly/eDAssembly_Class.htm), respectively.

1. Repeat Steps 5 and 6 to create additional components.
2. Repeat Steps 3 - 6 to create additional configurations.
3. Create the serialization object ([eDSerializer](../eDSerializer/eDSerializer_Class.htm)) from [eDScene::CreateSerializer](../eDScene/eDScene_Class.htm).
4. Save the scene to disk using [eDSerializer::Serialize](../eDSerializer/eDSerializer_Class.htm) with [eDSerializerParams](../eDSerializerParams/eDSerializerParams_Class.htm) as a parameter.
