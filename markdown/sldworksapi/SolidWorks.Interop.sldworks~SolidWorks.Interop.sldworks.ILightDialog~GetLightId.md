---
title: "GetLightId Method (ILightDialog)"
project: "SOLIDWORKS API Help"
interface: "ILightDialog"
member: "GetLightId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog~GetLightId.html"
---

# GetLightId Method (ILightDialog)

Gets the ID of the edited light in the light dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLightId() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILightDialog
Dim value As System.Integer

value = instance.GetLightId()
```

### C#

```csharp
System.int GetLightId()
```

### C++/CLI

```cpp
System.int GetLightId();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

ID of the light currently being modified by the dialog; -1 if the light cannot be found

## VBA Syntax

See [LightDialog::GetLightId](ms-its:sldworksapivb6.chm::/sldworks~LightDialog~GetLightId.html).

## See Also

[ILightDialog Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog.html)
[ILightDialog Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog_members.html)

## Availability

SOLIDWORKS 99, Revision Number 1999207
