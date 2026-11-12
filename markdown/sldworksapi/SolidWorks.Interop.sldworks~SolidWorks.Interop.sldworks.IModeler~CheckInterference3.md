---
title: "CheckInterference3 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CheckInterference3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.html"
---

# CheckInterference3 Method (IModeler)

Checks for interferences among the specified bodies in a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function CheckInterference3( _
   ByVal TargetBodies As System.Object, _
   ByVal ToolBodies As System.Object, _
   ByVal Options As System.Integer, _
   ByRef Body1InterferedFaceArray As System.Object, _
   ByRef Body2InterferedFaceArray As System.Object, _
   ByRef IntersectedBodyArray As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim TargetBodies As System.Object
Dim ToolBodies As System.Object
Dim Options As System.Integer
Dim Body1InterferedFaceArray As System.Object
Dim Body2InterferedFaceArray As System.Object
Dim IntersectedBodyArray As System.Object
Dim value As System.Boolean

value = instance.CheckInterference3(TargetBodies, ToolBodies, Options, Body1InterferedFaceArray, Body2InterferedFaceArray, IntersectedBodyArray)
```

### C#

```csharp
System.bool CheckInterference3(
   System.object TargetBodies,
   System.object ToolBodies,
   System.int Options,
   out System.object Body1InterferedFaceArray,
   out System.object Body2InterferedFaceArray,
   out System.object IntersectedBodyArray
)
```

### C++/CLI

```cpp
System.bool CheckInterference3(
   System.Object^ TargetBodies,
   System.Object^ ToolBodies,
   System.int Options,
   [Out] System.Object^ Body1InterferedFaceArray,
   [Out] System.Object^ Body2InterferedFaceArray,
   [Out] System.Object^ IntersectedBodyArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TargetBodies`: Target [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `ToolBodies`: Tool [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `Options`: Check interference options as defined by [swCheckInterferenceOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCheckInterferenceOption_e.html)
- `Body1InterferedFaceArray`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that interfered from the first body with the second body
- `Body2InterferedFaceArray`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that interfered from the second body with the first body
- `IntersectedBodyArray`: Array of interfering [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

### Return Value

True if an interference exists, false if not

## VBA Syntax

See [Modeler::CheckInterference3](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CheckInterference3.html).

## Examples

[Check Interference Among Bodies (VBA)](Check_Interference_Among_Bodies_Example_VB.htm)

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.html)
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.html)
[IAssemblyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html)
[IAssemblyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.html)
[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IModeler::CheckInterferenceBetweenTwoBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterferenceBetweenTwoBodies.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
