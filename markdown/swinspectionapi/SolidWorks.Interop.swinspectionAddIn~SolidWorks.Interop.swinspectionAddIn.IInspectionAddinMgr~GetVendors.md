---
title: "GetVendors Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "GetVendors"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~GetVendors.html"
---

# GetVendors Method (IInspectionAddinMgr)

Gets the list of vendors.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVendors( _
   ByRef VendorList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim VendorList As System.Object
Dim value As System.Boolean

value = instance.GetVendors(VendorList)
```

### C#

```csharp
System.bool GetVendors(
   out System.object VendorList
)
```

### C++/CLI

```cpp
System.bool GetVendors(
   [Out] System.Object^ VendorList
)
```

### Parameters

- `VendorList`: Array of vendors

### Return Value

True if vendors successfully retrieved, false if not

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
