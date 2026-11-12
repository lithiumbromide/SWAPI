---
title: "RadiationEndEdit Method (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "RadiationEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~RadiationEndEdit.html"
---

# RadiationEndEdit Method (ICWRadiation)

Ends editing radiation.

## Syntax

### Visual Basic (Declaration)

```vb
Function RadiationEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
Dim value As System.Integer

value = instance.RadiationEndEdit()
```

### C#

```csharp
System.int RadiationEndEdit()
```

### C++/CLI

```cpp
System.int RadiationEndEdit();
```

### Return Value

Error as defined in [swsRadiationEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRadiationEndEditError_e.html)

## VBA Syntax

See [CWRadiation::RadiationEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~RadiationEndEdit.html).

## Examples

See the [ICWRadiation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html) examples.

## Remarks

You must call [ICWRadiation::RadiationBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPressure~PressureBeginEdit.html) to start editing radiation. To end editing radiation, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
