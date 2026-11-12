---
title: "AddVendor Method (InspectionAddinMgrClass)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionAddinMgrClass"
member: "AddVendor"
kind: "method"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass~AddVendor.html"
---

# AddVendor Method (InspectionAddinMgrClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Function AddVendor( _
   ByVal VendorName As System.String, _
   ByVal VendorType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionAddinMgrClass
Dim VendorName As System.String
Dim VendorType As System.Integer
Dim value As System.Boolean

value = instance.AddVendor(VendorName, VendorType)
```

### C#

```csharp
public virtual System.bool AddVendor(
   System.string VendorName,
   System.int VendorType
)
```

### C++/CLI

```cpp
public:
virtual System.bool AddVendor(
   System.String^ VendorName,
   System.int VendorType
)
```

### Parameters

- `VendorName`:
- `VendorType`:

## See Also

[InspectionAddinMgrClass Class](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass.html)
[InspectionAddinMgrClass Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionAddinMgrClass_members.html)
