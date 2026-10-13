---
title: "AddPagex64 Method (ISWPropertySheet)"
project: "SOLIDWORKS API Help"
interface: "ISWPropertySheet"
member: "AddPagex64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddPagex64.html"
---

# AddPagex64 Method (ISWPropertySheet)

Adds a CPropertyPage-derived page to an [ISWPropertySheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html) in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPagex64( _
   ByVal Page As System.Long _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWPropertySheet
Dim Page As System.Long
Dim value As System.Integer

value = instance.AddPagex64(Page)
```

### C#

```csharp
System.int AddPagex64(
   System.long Page
)
```

### C++/CLI

```cpp
System.int AddPagex64(
   System.int64 Page
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Page`: Pointer to the CPropertyPage to add, cast to a long long

### Return Value

True if successful, false if not

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

## See Also

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.html)
[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.html)
[ISWPropertySheet::AddPage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddPage.html)

## Availability

SOLIDWORKS 2010 SP01, Revision Number 18.1
