---
title: "CFForceBeginEdit Method (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "CFForceBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~CFForceBeginEdit.html"
---

# CFForceBeginEdit Method (ICWCentriFugalForce)

Starts editing a centrifugal force.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CFForceBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce

instance.CFForceBeginEdit()
```

### C#

```csharp
void CFForceBeginEdit()
```

### C++/CLI

```cpp
void CFForceBeginEdit();
```

## VBA Syntax

See [CWCentriFugalForce::CFForceBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCentriFugalForce~CFForceBeginEdit.html).

## Examples

See the [ICWCentriFugalForce](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html) examples.

## Remarks

To start editing a centrifugal force, you must call this method. You must call [ICWCentrifugalForce::CFForceEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWCentriFugalForce~CFForceEndEdit.html) to end editing the centrifugal force. Changes are not applied unless you call both methods.

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
