---
title: "GetTableAnnotations Method (IWeldmentCutListFeature)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListFeature"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IWeldmentCutListFeature)

Gets the weldment cut list annotations for this weldment cut list table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListFeature
Dim value As System.Object

value = instance.GetTableAnnotations()
```

### C#

```csharp
System.object GetTableAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetTableAnnotations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [weldment cut-list annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListAnnotation.html) for this weldment cut list table

## VBA Syntax

See [WeldmentCutListFeature::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListFeature~GetTableAnnotations.html).

## Examples

See the [IWeldmentCutListFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html) examples.

## See Also

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html)
[IWeldmentCutListFeature::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~IGetTableAnnotations.html)
[IWeldmentCutListFeature::GetTableAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotationCount.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
