---
title: "AddItems Method (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "AddItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~AddItems.html"
---

# AddItems Method (IPropertyManagerPageListbox)

Adds items to the attached drop-down list for this list box.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddItems( _
   ByVal Texts As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
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

- `Texts`: Array of strings of the items

## VBA Syntax

See [PropertyManagerPageListbox::AddItems](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageListbox~AddItems.html).

## Examples

See the [IPropertyManagerPageListbox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html) examples.

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)
[IPropertyManagerPageListbox::IAddItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~IAddItems.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
