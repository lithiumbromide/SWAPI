---
title: "RemovePage Method (ISWPropertySheet)"
project: "SOLIDWORKS API Help"
interface: "ISWPropertySheet"
member: "RemovePage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~RemovePage.html"
---

# RemovePage Method (ISWPropertySheet)

Removes a CPropertyPage derived page from an [ISWPropertySheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemovePage( _
   ByVal Page As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWPropertySheet
Dim Page As System.Integer
Dim value As System.Integer

value = instance.RemovePage(Page)
```

### C#

```csharp
System.int RemovePage(
   System.int Page
)
```

### C++/CLI

```cpp
System.int RemovePage(
   System.int Page
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Page`: CPropertyPage to add, cast to a long

### Return Value

True if successful, false if not

## VBA Syntax

See [SWPropertySheet::RemovePage](ms-its:sldworksapivb6.chm::/sldworks~SWPropertySheet~RemovePage.html).

## See Also

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.html)
[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.html)
