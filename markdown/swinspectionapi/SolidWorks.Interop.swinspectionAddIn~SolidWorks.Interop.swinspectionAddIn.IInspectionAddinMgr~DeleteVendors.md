---
title: "DeleteVendors Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "DeleteVendors"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~DeleteVendors.html"
---

# DeleteVendors Method (IInspectionAddinMgr)

Deletes the specified vendors.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteVendors( _
   ByRef VendorList As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim VendorList As System.Object
Dim value As System.Object

value = instance.DeleteVendors(VendorList)
```

### C#

```csharp
System.object DeleteVendors(
   ref System.object VendorList
)
```

### C++/CLI

```cpp
System.Object^ DeleteVendors(
   System.Object^% VendorList
)
```

### Parameters

- `VendorList`: Array of vendors to delete

### Return Value

Array of booleans indicating whether each vendor is successfully deleted

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
