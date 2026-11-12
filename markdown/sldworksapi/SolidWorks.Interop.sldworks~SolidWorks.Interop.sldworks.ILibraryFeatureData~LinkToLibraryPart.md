---
title: "LinkToLibraryPart Property (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "LinkToLibraryPart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LinkToLibraryPart.html"
---

# LinkToLibraryPart Property (ILibraryFeatureData)

Gets or sets whether to the link the library feature to its parent library feature document.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkToLibraryPart As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim value As System.Boolean

instance.LinkToLibraryPart = value

value = instance.LinkToLibraryPart
```

### C#

```csharp
System.bool LinkToLibraryPart {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkToLibraryPart {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to link the library feature to its parent library feature document, false to not

## VBA Syntax

See [LibraryFeatureData::LinkToLibraryPart](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~LinkToLibraryPart.html).

## Examples

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::LibraryPart Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~LibraryPart.html)
[ILibraryFeatureData::Initialize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~Initialize.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
