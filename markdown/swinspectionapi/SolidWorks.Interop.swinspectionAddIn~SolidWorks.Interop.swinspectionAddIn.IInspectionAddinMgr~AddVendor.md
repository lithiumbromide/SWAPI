---
title: "AddVendor Method (IInspectionAddinMgr)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionAddinMgr"
member: "AddVendor"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr~AddVendor.html"
---

# AddVendor Method (IInspectionAddinMgr)

Adds the specified vendor to the list of vendors.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddVendor( _
   ByVal VendorName As System.String, _
   ByVal VendorType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionAddinMgr
Dim VendorName As System.String
Dim VendorType As System.Integer
Dim value As System.Boolean

value = instance.AddVendor(VendorName, VendorType)
```

### C#

```csharp
System.bool AddVendor(
   System.string VendorName,
   System.int VendorType
)
```

### C++/CLI

```cpp
System.bool AddVendor(
   System.String^ VendorName,
   System.int VendorType
)
```

### Parameters

- `VendorName`: Name of vendor
- `VendorType`: Type of vendor as defined by [swiVendorsInspectionType_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiVendorsInspectionType_e.html)

## VBA Syntax

See [InspectionAddinMgr](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionAddinMgr_members.html) methods.

## See Also

[IInspectionAddinMgr Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr.html)
[IInspectionAddinMgr Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionAddinMgr_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
