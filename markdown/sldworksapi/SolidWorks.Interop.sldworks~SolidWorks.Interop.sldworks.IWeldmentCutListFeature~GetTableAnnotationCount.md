---
title: "GetTableAnnotationCount Method (IWeldmentCutListFeature)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListFeature"
member: "GetTableAnnotationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotationCount.html"
---

# GetTableAnnotationCount Method (IWeldmentCutListFeature)

Gets the number of weldment cut list annotations for this weldment cut list table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListFeature
Dim value As System.Integer

value = instance.GetTableAnnotationCount()
```

### C#

```csharp
System.int GetTableAnnotationCount()
```

### C++/CLI

```cpp
System.int GetTableAnnotationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of weldment cut list annotations for this weldment cut list table

## VBA Syntax

See [WeldmentCutListFeature::GetTableAnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListFeature~GetTableAnnotationCount.html).

## Remarks

Call this method before calling [IWeldmentCutListFeature::IGetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListFeature~IGetTableAnnotations.html) to get the size of the array for that method.

## See Also

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html)
[IWeldmentCutListFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
