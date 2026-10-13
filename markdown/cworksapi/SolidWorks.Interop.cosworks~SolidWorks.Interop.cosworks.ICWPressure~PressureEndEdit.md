---
title: "PressureEndEdit Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "PressureEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~PressureEndEdit.html"
---

# PressureEndEdit Method (ICWPressure)

Ends editing pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Function PressureEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Integer

value = instance.PressureEndEdit()
```

### C#

```csharp
System.int PressureEndEdit()
```

### C++/CLI

```cpp
System.int PressureEndEdit();
```

### Return Value

Error as defined in [swsPressureEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPressureEndEditError_e.html)

## VBA Syntax

See [CWPressure::PressureEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~PressureEndEdit.html).

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## Remarks

You must call [ICWPressure::PressureBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPressure~PressureBeginEdit.html) to start editing pressure. To end editing pressure, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
