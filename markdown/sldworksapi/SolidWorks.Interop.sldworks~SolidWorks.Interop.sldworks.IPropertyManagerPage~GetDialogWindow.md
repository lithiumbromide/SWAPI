---
title: "GetDialogWindow Method (IPropertyManagerPage)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage"
member: "GetDialogWindow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage~GetDialogWindow.html"
---

# GetDialogWindow Method (IPropertyManagerPage)

Obsolete. Not superseded.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDialogWindow( _
   ByRef Status As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage
Dim Status As System.Integer
Dim value As System.Integer

value = instance.GetDialogWindow(Status)
```

### C#

```csharp
System.int GetDialogWindow(
   out System.int Status
)
```

### C++/CLI

```cpp
System.int GetDialogWindow(
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Status`:

## VBA Syntax

See [PropertyManagerPage::GetDialogWindow](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage~GetDialogWindow.html).

## See Also

[IPropertyManagerPage Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage.html)
[IPropertyManagerPage Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage_members.html)
