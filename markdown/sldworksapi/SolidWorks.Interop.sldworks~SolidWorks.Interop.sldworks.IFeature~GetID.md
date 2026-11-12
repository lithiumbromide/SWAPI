---
title: "GetID Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetID.html"
---

# GetID Method (IFeature)

Gets the feature ID of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.GetID()
```

### C#

```csharp
System.int GetID()
```

### C++/CLI

```cpp
System.int GetID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Feature ID of this feature

## VBA Syntax

See [Feature::GetID](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetID.html).

## Examples

[Get Type of Instant3D Feature (C#)](Get_Type_of_Instant3D_Feature_Example_CSharp.htm)
[Get Type of Instant3D Feature (VB.NET)](Get_Type_of_Instant3D_Feature_Example_VBNET.htm)
[Get Type of Instant3D Feature (VBA)](Get_Type_of_Instant3D_Feature_Example_VB.htm)

## Remarks

A feature ID:

- is unique within the document.
- is persistent across SOLIDWORKS Design sessions and never changes, even if you [change the name of the feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.html).
- can be used to identify a specific feature when multiple features exist in a model.
- cannot be assigned by users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get a feature using its persistent reference ID, but you cannot get a feature using this method.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

## Availability

SOLIDWORKS 2014, FCS Revision Number 22.0
