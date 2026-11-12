---
title: "OnTabClicked Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnTabClicked"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnTabClicked.html"
---

# OnTabClicked Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnTabClicked](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnTabClicked.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnTabClicked( _
   ByVal Id As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler5
Dim Id As System.Integer
Dim value As System.Boolean

value = instance.OnTabClicked(Id)
```

### C#

```csharp
System.bool OnTabClicked(
   System.int Id
)
```

### C++/CLI

```cpp
System.bool OnTabClicked(
   System.int Id
)
```

### Parameters

- `Id`: ID of the tab clicked (see Remarks)

### Return Value

True if the tab clicked is processed, false if not

## VBA Syntax

See [PropertyManagerPage2Handler5::OnTabClicked](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnTabClicked.html).

## Remarks

The value of Id is the ID that was specified when the tab was created by [IPropertyManagerPage2::AddTab](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddTab.html).

When a user clicks a tab, control is passed to the add-in via this method. The add-in is expected to show or hide groups and controls intended to be visible or hidden on that tab.

Your add-in is responsible for showing and hiding the controls on a tab to simulate moving between tabs, making it look like the tab is a container for the controls. However, tabs are not containers for the groups or controls. Tabs are controls that are displayed in a certain way, making them look like control containers.

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 16.0
