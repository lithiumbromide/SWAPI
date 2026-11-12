---
title: "IMargins Property (CostAnalysisMachiningClass)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachiningClass"
member: "IMargins"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass~IMargins.html"
---

# IMargins Property (CostAnalysisMachiningClass)

## Syntax

### Visual Basic (Declaration)

```vb
Public Overridable Property IMargins( _
   ByVal NumDimensions As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachiningClass
Dim NumDimensions As System.Integer
Dim value As System.Double

instance.IMargins(NumDimensions) = value

value = instance.IMargins(NumDimensions)
```

### C#

```csharp
public virtual System.double IMargins(
   System.int NumDimensions
) {get; set;}
```

### C++/CLI

```cpp
public:
virtual property System.double IMargins {
   System.double get(System.int NumDimensions);
   void set (System.int NumDimensions, System.double value);
}
```

### Parameters

- `NumDimensions`:

## See Also

[CostAnalysisMachiningClass Class](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass.html)
[CostAnalysisMachiningClass Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachiningClass_members.html)
