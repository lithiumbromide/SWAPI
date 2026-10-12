---
title: "ICheckInterference3 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICheckInterference3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.html"
---

# ICheckInterference3 Method (IModeler)

Checks the interference among the specified bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICheckInterference3( _
   ByRef Body1InterferedFaceArray As Face2, _
   ByRef Body2InterferedFaceArray As Face2, _
   ByRef IntersectedBodyArray As Body2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Body1InterferedFaceArray As Face2
Dim Body2InterferedFaceArray As Face2
Dim IntersectedBodyArray As Body2
Dim value As System.Boolean

value = instance.ICheckInterference3(Body1InterferedFaceArray, Body2InterferedFaceArray, IntersectedBodyArray)
```

### C#

```csharp
System.bool ICheckInterference3(
   out Face2 Body1InterferedFaceArray,
   out Face2 Body2InterferedFaceArray,
   out Body2 IntersectedBodyArray
)
```

### C++/CLI

```cpp
System.bool ICheckInterference3(
   [Out] Face2^ Body1InterferedFaceArray,
   [Out] Face2^ Body2InterferedFaceArray,
   [Out] Body2^ IntersectedBodyArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body1InterferedFaceArray`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that have interfered from the first body with the second body
- `Body2InterferedFaceArray`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that interfered from the second body with the first body
- `IntersectedBodyArray`: Array of interfering [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

### Return Value

True if a clash occurred, false if not

## VBA Syntax

See [Modeler::ICheckInterference3](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICheckInterference3.html).

## Remarks

Before calling this method, call [IModeler::ICheckInterferenceCount3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICheckInterferenceCount3.html) to allocate memory for the arrays returned from this method.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IAssemblyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html)
[IAssemblyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.html)
[IModeler::CheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference3.html)
[IModeler::ICheckInterferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount3.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
