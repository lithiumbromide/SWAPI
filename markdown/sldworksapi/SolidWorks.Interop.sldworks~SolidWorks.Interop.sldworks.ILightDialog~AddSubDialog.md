---
title: "AddSubDialog Method (ILightDialog)"
project: "SOLIDWORKS API Help"
interface: "ILightDialog"
member: "AddSubDialog"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog~AddSubDialog.html"
---

# AddSubDialog Method (ILightDialog)

Adds a sub-dialog to the lighting dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSubDialog( _
   ByVal Page As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILightDialog
Dim Page As System.Integer
Dim value As System.Boolean

value = instance.AddSubDialog(Page)
```

### C#

```csharp
System.bool AddSubDialog(
   System.int Page
)
```

### C++/CLI

```cpp
System.bool AddSubDialog(
   System.int Page
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Page`: Pointer to a CDialog object cast to a long

### Return Value

True if the dialog was successfully added, false if not

## VBA Syntax

See [LightDialog::AddSubDialog](ms-its:sldworksapivb6.chm::/sldworks~LightDialog~AddSubDialog.html).

## Remarks

Currently only one sub-dialog can be added to each dialog.

## See Also

[ILightDialog Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog.html)
[ILightDialog Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
