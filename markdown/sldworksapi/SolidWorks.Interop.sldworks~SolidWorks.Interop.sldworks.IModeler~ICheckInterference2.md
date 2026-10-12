---
title: "ICheckInterference2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICheckInterference2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference2.html"
---

# ICheckInterference2 Method (IModeler)

Obsolete. Superseded by [IModeler::ICheckInterference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICheckInterference3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICheckInterference2( _
   ByRef Body1InterferedFaceArray As Face2, _
   ByRef Body2InterferedFaceArray As Face2, _
   ByRef IntersectedBodyArray As Body2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Body1InterferedFaceArray As Face2
Dim Body2InterferedFaceArray As Face2
Dim IntersectedBodyArray As Body2

instance.ICheckInterference2(Body1InterferedFaceArray, Body2InterferedFaceArray, IntersectedBodyArray)
```

### C#

```csharp
void ICheckInterference2(
   out Face2 Body1InterferedFaceArray,
   out Face2 Body2InterferedFaceArray,
   out Body2 IntersectedBodyArray
)
```

### C++/CLI

```cpp
void ICheckInterference2(
   [Out] Face2^ Body1InterferedFaceArray,
   [Out] Face2^ Body2InterferedFaceArray,
   [Out] Body2^ IntersectedBodyArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body1InterferedFaceArray`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that interfered from the first body with the second body
- `Body2InterferedFaceArray`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that interfered from the second body with the first body
- `IntersectedBodyArray`: [Bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) generated from the intersection of the input bodies

## VBA Syntax

See [Modeler::ICheckInterference2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICheckInterference2.html).

## Remarks

Before calling this method, call [IModeler::ICheckInterferenceCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICheckInterferenceCount2.html) to allocate memory for the arrays returned from this method.

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CheckInterference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference.html)
[IAssembyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html)
[IAssembyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
