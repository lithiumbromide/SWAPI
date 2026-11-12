---
title: "UpdateDialog Method (IPrint3DDialog)"
project: "SOLIDWORKS API Help"
interface: "IPrint3DDialog"
member: "UpdateDialog"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrint3DDialog~UpdateDialog.html"
---

# UpdateDialog Method (IPrint3DDialog)

Updates the build statistics on the Print 3D dialog for a local 3D printer.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateDialog() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrint3DDialog
Dim value As System.Boolean

value = instance.UpdateDialog()
```

### C#

```csharp
System.bool UpdateDialog()
```

### C++/CLI

```cpp
System.bool UpdateDialog();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the statistics are updated, false if not

## VBA Syntax

See [Print3DDialog::UpdateDialog](ms-its:sldworksapivb6.chm::/sldworks~Print3DDialog~UpdateDialog.html).

## See Also

[IPrint3DDialog Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrint3DDialog.html)
[IPrint3DDialog Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrint3DDialog_members.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15.1
