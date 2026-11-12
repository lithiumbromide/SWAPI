---
title: "AddTab Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "AddTab"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddTab.html"
---

# AddTab Method (IPropertyManagerPage2)

Adds a tab to a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddTab( _
   ByVal ID As System.Integer, _
   ByVal Caption As System.String, _
   ByVal Bitmap As System.String, _
   ByVal Options As System.Integer _
) As PropertyManagerPageTab
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim ID As System.Integer
Dim Caption As System.String
Dim Bitmap As System.String
Dim Options As System.Integer
Dim value As PropertyManagerPageTab

value = instance.AddTab(ID, Caption, Bitmap, Options)
```

### C#

```csharp
PropertyManagerPageTab AddTab(
   System.int ID,
   System.string Caption,
   System.string Bitmap,
   System.int Options
)
```

### C++/CLI

```cpp
PropertyManagerPageTab^ AddTab(
   System.int ID,
   System.String^ Caption,
   System.String^ Bitmap,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Identifier defined by the add-in for this tab
- `Caption`: Text for tab
- `Bitmap`: Bitmap for tab
- `Options`: Not used; specify 0

### Return Value

Newly created [PropertyManager page tab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageTab.html)

## VBA Syntax

See [PropertyManagerPage2::AddTab](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~AddTab.html).

## Remarks

The ID argument provides an add-in with a way of identifying which tab is being handled when one of the callbacks is called; for example, when [IPropertyManagerPage2Handler8::OnTabClicked](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnTabClicked.html) is called. The IDis passed as an argument, identifying the tab clicked.

The Bitmap argument allows you to place a bitmap before the text on the tab. The argument is the full path and filename to a bitmap on disk. The bitmap should be 16 x 18 (width x height) pixels. It can be either 16 or 256 colors. Any portions of the bitmap that are RGB(255,255,255) will be transparent, letting the tab background show through. If this argument is an empty string or not the name of a valid bitmap file, no bitmap is placed on the tab.

Use this method to add tabs to your PropertyManager page before the page is displayed. It cannot be used if the page is already displayed.

Use [IPropertyManagerPageTab::Caption](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageTab~Caption.html) to add a caption to the tab.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
