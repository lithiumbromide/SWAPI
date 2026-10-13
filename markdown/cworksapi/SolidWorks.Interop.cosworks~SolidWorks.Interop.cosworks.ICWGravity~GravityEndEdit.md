---
title: "GravityEndEdit Method (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "GravityEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~GravityEndEdit.html"
---

# GravityEndEdit Method (ICWGravity)

Ends editing gravity.

## Syntax

### Visual Basic (Declaration)

```vb
Function GravityEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
Dim value As System.Integer

value = instance.GravityEndEdit()
```

### C#

```csharp
System.int GravityEndEdit()
```

### C++/CLI

```cpp
System.int GravityEndEdit();
```

### Return Value

Error as defined in [swsGravityEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsGravityEndEditError_e.html)

## VBA Syntax

See [CWGravity::GravityEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGravity~GravityEndEdit.html).

## Remarks

To end editing gravity, you must call this method. You must call [ICWGravity::GravityBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWGravity~GravityBeginEdit.html) to start editing gravity. Changes are not applied unless you call both methods.

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
