---
title: "IAddItems Method (IPropertyManagerPageListbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageListbox"
member: "IAddItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~IAddItems.html"
---

# IAddItems Method (IPropertyManagerPageListbox)

Adds items to the attached drop-down list for this list box.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IAddItems( _
   ByVal TextCount As System.Short, _
   ByRef Texts As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageListbox
Dim TextCount As System.Short
Dim Texts As System.String

instance.IAddItems(TextCount, Texts)
```

### C#

```csharp
void IAddItems(
   System.short TextCount,
   ref System.string Texts
)
```

### C++/CLI

```cpp
void IAddItems(
   System.short TextCount,
   System.String^% Texts
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TextCount`: Number of items to add to the listbox
- `Texts`: - in-process, unmanaged C++: Pointer to an array of strings of items of size TextCount
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.html)
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html)
[IPropertyManagerPageListbox::AddItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~AddItems.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
