---
title: "IAddItems Method (IPropertyManagerPageNumberbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageNumberbox"
member: "IAddItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~IAddItems.html"
---

# IAddItems Method (IPropertyManagerPageNumberbox)

Adds items to the attached drop-down list of a number box.

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
Dim instance As IPropertyManagerPageNumberbox
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
- `Texts`: - in-process, unmanaged C++: Pointer to an array of strings of items

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.html)
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html)
[IPropertyManagerPageNumberbox::AddItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~AddItems.html)
