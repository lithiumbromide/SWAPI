---
title: "GetMotionStudyManager Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetMotionStudyManager"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMotionStudyManager.html"
---

# GetMotionStudyManager Method (IModelDocExtension)

Gets the SOLIDWORKS motion study's MotionManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMotionStudyManager() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetMotionStudyManager()
```

### C#

```csharp
System.object GetMotionStudyManager()
```

### C++/CLI

```cpp
System.Object^ GetMotionStudyManager();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[MotionManager](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyManager.html)

## VBA Syntax

See [ModelDocExtension::GetMotionStudyManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetMotionStudyManager.html).

## Examples

[Create Motion Studies (VBA)](Create_Motion_Studies_Example_VB.htm)
[Get COSMOSMotion Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)
[Get Motion Study (VBA)](Get_Motion_Study_Example_VB.htm)
[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)
[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
