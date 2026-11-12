---
title: "AddItems Method (IPropertyManagerPageCombobox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCombobox"
member: "AddItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~AddItems.html"
---

# AddItems Method (IPropertyManagerPageCombobox)

Adds items to the attached drop-down list for this combo box.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddItems( _
   ByVal Texts As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageCombobox
Dim Texts As System.Object

instance.AddItems(Texts)
```

### C#

```csharp
void AddItems(
   System.object Texts
)
```

### C++/CLI

```cpp
void AddItems(
   System.Object^ Texts
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Texts`: Array of strings of items

## VBA Syntax

See [PropertyManagerPageCombobox::AddItems](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageCombobox~AddItems.html).

## Examples

See the [IPropertyManagerPageCombobox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html) examples.

## See Also

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html)
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.html)
[IPropertyManagerPageCombobox::IAddItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~IAddItems.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
