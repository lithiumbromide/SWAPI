---
title: "ForceEndEdit Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "ForceEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceEndEdit.html"
---

# ForceEndEdit Method (ICWForce)

Ends editing a force.

## Syntax

### Visual Basic (Declaration)

```vb
Function ForceEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Integer

value = instance.ForceEndEdit()
```

### C#

```csharp
System.int ForceEndEdit()
```

### C++/CLI

```cpp
System.int ForceEndEdit();
```

### Return Value

Error as defined in [swsForceEndEditError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceEndEditError_e.html)

## VBA Syntax

See [CWForce::ForceEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~ForceEndEdit.html).

## Examples

[Add Nonuniform Force Distribution (VBA)](Add_Force_Example_VB.htm)
[Add Nonuniform Force Distribution (VB.NET)](Add_Force_Example_VBNET.htm)
[Add Nonuniform Force Distribution (C#)](Add_Force_Example_CSharp.htm)

## Remarks

You must call [ICWForce::ForceBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWForce~ForceBeginEdit.html) to start editing this force. To end editing this force, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
