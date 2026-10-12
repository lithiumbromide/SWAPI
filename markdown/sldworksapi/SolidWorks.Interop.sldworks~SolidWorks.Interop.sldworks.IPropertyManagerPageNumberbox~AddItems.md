---
title: "AddItems Method (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "AddItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~AddItems.html"
---

# AddItems Method (IPropertyManagerPageNumberbox)

Adds items to the attached drop-down list of a number box.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddItems( _
   ByVal Texts As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageNumberbox
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

See [PropertyManagerPageNumberbox::AddItems](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageNumberbox~AddItems.html).

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)
[IPropertyManagerPageNumberbox::IAddItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~IAddItems.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
