---
title: "CFForceEndEdit Method (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "CFForceEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~CFForceEndEdit.html"
---

# CFForceEndEdit Method (ICWCentriFugalForce)

Ends editing of a centrifugal force.

## Syntax

### Visual Basic (Declaration)

```vb
Function CFForceEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
Dim value As System.Integer

value = instance.CFForceEndEdit()
```

### C#

```csharp
System.int CFForceEndEdit()
```

### C++/CLI

```cpp
System.int CFForceEndEdit();
```

### Return Value

Error as defined in [swsCentrifugalForceEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsCentrifugalForceEndEditError_e.html)

## VBA Syntax

See [CWCentriFugalForce::CFForceEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCentriFugalForce~CFForceEndEdit.html).

## Examples

See the [ICWCentriFugalForce](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html) examples.

## Remarks

You must call [ICWCentrifugalForce::CFForceBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWCentriFugalForce~CFForceBeginEdit.html) to start editing a centrifugal force. To end editing a centrifugal force, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
