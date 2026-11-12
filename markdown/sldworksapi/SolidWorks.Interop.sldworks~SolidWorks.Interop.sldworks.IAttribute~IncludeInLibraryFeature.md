---
title: "IncludeInLibraryFeature Property (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "IncludeInLibraryFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IncludeInLibraryFeature.html"
---

# IncludeInLibraryFeature Property (IAttribute)

Gets or sets whether this attribute is included in the library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeInLibraryFeature As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim value As System.Boolean

instance.IncludeInLibraryFeature = value

value = instance.IncludeInLibraryFeature
```

### C#

```csharp
System.bool IncludeInLibraryFeature {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeInLibraryFeature {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the attribute is included in the library feature, false if not

## VBA Syntax

See [Attribute::IncludeInLibraryFeature](ms-its:sldworksapivb6.chm::/sldworks~Attribute~IncludeInLibraryFeature.html).

## Examples

[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)

## Remarks

Attributes included in a library feature are propagated to each instance of that library feature. However, If an entity (e.g., face, edge, etc.) is shared among features and all of these features are not included in the library feature, then the attribute is not propagated.

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
