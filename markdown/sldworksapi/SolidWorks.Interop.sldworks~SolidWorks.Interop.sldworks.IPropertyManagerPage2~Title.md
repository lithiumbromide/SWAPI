---
title: "Title Property (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "Title"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Title.html"
---

# Title Property (IPropertyManagerPage2)

Gets or sets the title of the PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property Title As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim value As System.String

instance.Title = value

value = instance.Title
```

### C#

```csharp
System.string Title {get; set;}
```

### C++/CLI

```cpp
property System.String^ Title {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Title of PropertyManager page

## VBA Syntax

See [PropertyManagerPage2::Title](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~Title.html).

## Remarks

You can use this method whether the page is displayed or not.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[IPropertyManagerPage2::SetTitleBitmap2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
