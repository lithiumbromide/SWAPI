---
title: "ForceBeginEdit Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "ForceBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceBeginEdit.html"
---

# ForceBeginEdit Method (ICWForce)

Starts editing a force.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ForceBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce

instance.ForceBeginEdit()
```

### C#

```csharp
void ForceBeginEdit()
```

### C++/CLI

```cpp
void ForceBeginEdit();
```

## VBA Syntax

See [CWForce::ForceBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~ForceBeginEdit.html).

## Examples

[Add Nonuniform Force Distribution (VBA)](Add_Force_Example_VB.htm)
[Add Nonuniform Force Distribution (VB.NET)](Add_Force_Example_VBNET.htm)
[Add Nonuniform Force Distribution (C#)](Add_Force_Example_CSharp.htm)

## Remarks

To start editing this force, you must call this method. You must call [ICWForce::ForceEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWForce~ForceEndEdit.html) to end editing this force. Changes are not applied unless you call both methods.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
