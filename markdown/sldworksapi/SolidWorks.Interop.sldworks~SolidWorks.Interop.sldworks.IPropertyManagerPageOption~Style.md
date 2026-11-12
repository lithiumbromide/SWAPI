---
title: "Style Property (IPropertyManagerPageOption)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageOption"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageOption~Style.html"
---

# Style Property (IPropertyManagerPageOption)

Gets or sets style-related properties for an option on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageOption
Dim value As System.Integer

instance.Style = value

value = instance.Style
```

### C#

```csharp
System.int Style {get; set;}
```

### C++/CLI

```cpp
property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Option style as defined in [swPropMgrPageOptionStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageOptionStyle_e.html)

## VBA Syntax

See [PropertyManagerPageOption::Style](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageOption~Style.html).

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

## See Also

[IPropertyManagerPageOption Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageOption.html)
[IPropertyManagerPageOption Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageOption_members.html)

## Availability

SOLIDWORKS 2001Plus SP4, Revision Number 10.4
