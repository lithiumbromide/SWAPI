---
title: "ICheckInterferenceCount3 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICheckInterferenceCount3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3.html"
---

# ICheckInterferenceCount3 Method (IModeler)

Checks interference among the specified bodies and returns the number of interferences.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICheckInterferenceCount3( _
   ByVal NumOfTargetBodies As System.Integer, _
   ByRef TargetBodies As Body2, _
   ByVal NumOfToolBodies As System.Integer, _
   ByRef ToolBodies As Body2, _
   ByVal Options As System.Integer, _
   ByRef NumBody1InterferedFaceArray As System.Integer, _
   ByRef NumBody2InterferedFaceArray As System.Integer, _
   ByRef NumIntersectedBodyArray As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NumOfTargetBodies As System.Integer
Dim TargetBodies As Body2
Dim NumOfToolBodies As System.Integer
Dim ToolBodies As Body2
Dim Options As System.Integer
Dim NumBody1InterferedFaceArray As System.Integer
Dim NumBody2InterferedFaceArray As System.Integer
Dim NumIntersectedBodyArray As System.Integer
Dim value As System.Boolean

value = instance.ICheckInterferenceCount3(NumOfTargetBodies, TargetBodies, NumOfToolBodies, ToolBodies, Options, NumBody1InterferedFaceArray, NumBody2InterferedFaceArray, NumIntersectedBodyArray)
```

### C#

```csharp
System.bool ICheckInterferenceCount3(
   System.int NumOfTargetBodies,
   ref Body2 TargetBodies,
   System.int NumOfToolBodies,
   ref Body2 ToolBodies,
   System.int Options,
   out System.int NumBody1InterferedFaceArray,
   out System.int NumBody2InterferedFaceArray,
   out System.int NumIntersectedBodyArray
)
```

### C++/CLI

```cpp
System.bool ICheckInterferenceCount3(
   System.int NumOfTargetBodies,
   Body2^% TargetBodies,
   System.int NumOfToolBodies,
   Body2^% ToolBodies,
   System.int Options,
   [Out] System.int NumBody1InterferedFaceArray,
   [Out] System.int NumBody2InterferedFaceArray,
   [Out] System.int NumIntersectedBodyArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfTargetBodies`: Number of target bodies
- `TargetBodies`: Array of target [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `NumOfToolBodies`: Number of tool bodies
- `ToolBodies`: Array of tool [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
- `Options`: Check interference options as defined by [swCheckInterferenceOption_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckInterferenceOption_e.html)
- `NumBody1InterferedFaceArray`: Number of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that interfered from the first body with the second body
- `NumBody2InterferedFaceArray`: Number of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that interfered from the second body with the first body
- `NumIntersectedBodyArray`: Number of interfering [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::ICheckInterferenceCount3](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICheckInterferenceCount3.html).

## Remarks

Call this method before calling [IModeler::ICheckInterference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICheckInterference3.html) to get the size of the arrays for that method.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ICheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.html)
[IModeler::CheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.html)
[IAssemblyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html)
[IAssemblyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
