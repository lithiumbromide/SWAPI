---
title: "IAddItems Method (IPropertyManagerPageCombobox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCombobox"
member: "IAddItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~IAddItems.html"
---

# IAddItems Method (IPropertyManagerPageCombobox)

Adds items to the attached drop-down list for this combo box.

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
Dim instance As IPropertyManagerPageCombobox
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

- `TextCount`: Number of items to add
- `Texts`: - in-process, unmanaged C++: Pointer to an array of strings of the items of size TextCount
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.html)
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.html)
[IPropertyManagerPageCombobox::AddItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~AddItems.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
