---
title: "GetEditStatus Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetEditStatus"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetEditStatus.html"
---

# GetEditStatus Method (IFeature)

Gets whether the feature can currently be edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEditStatus() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.GetEditStatus()
```

### C#

```csharp
System.int GetEditStatus()
```

### C++/CLI

```cpp
System.int GetEditStatus();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Editing status of feature as defined in [swFeatureEditStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureEditStatus_e.html)

## VBA Syntax

See [Feature::GetEditStatus](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetEditStatus.html).

## Examples

[Get Editing Status of Features (VB.NET)](Get_Editing_Status_of_Features_Example_VBNET.htm)
[Get Editing Status of Features (VBA)](Get_Editing_Status_of_Features_Example_VB.htm)
[Get Editing Status of Features (C#)](Get_Editing_Status_of_Features_Example_CSharp.htm)

## Remarks

Although swFeatureEditStatus_e is a bitmask, you currently cannot combine its mutually exclusive enumerators and you must examine the bit value of the return value for the editing status of the feature.

| If... | Then the return value will be... |
| --- | --- |
| a feature and all of its dependent items are not currently being edited | 0 (swFeature_Editable) for the feature and all of its dependent items |
| a feature is currently being edited | 1 (swFeature_NonEditable); this will also be the return value for all of the feature's dependent items |
| a sketch is currently being edited | 2 (swFeature_UnderEditing) |

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
