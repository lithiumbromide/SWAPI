---
title: "Caption Property (IPropertyManagerPageTab)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageTab"
member: "Caption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~Caption.html"
---

# Caption Property (IPropertyManagerPageTab)

Gets or sets the caption for this tab.

## Syntax

### Visual Basic (Declaration)

```vb
Property Caption As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageTab
Dim value As System.String

instance.Caption = value

value = instance.Caption
```

### C#

```csharp
System.string Caption {get; set;}
```

### C++/CLI

```cpp
property System.String^ Caption {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for tab caption

## VBA Syntax

See [PropertyManagerPageTab::Caption](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageTab~Caption.html).

## Remarks

You can reset a tab caption regardless if the PropertyManager page is displayed or hidden.

Use [IPropertyManagerPage2::AddTab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddTab.html) to add any number of tabs to your PropertyManager page.

## See Also

[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.html)
[IPropertyManagerPageTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
