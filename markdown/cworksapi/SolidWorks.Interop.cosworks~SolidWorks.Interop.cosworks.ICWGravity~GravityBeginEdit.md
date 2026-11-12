---
title: "GravityBeginEdit Method (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "GravityBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~GravityBeginEdit.html"
---

# GravityBeginEdit Method (ICWGravity)

Starts editing gravity.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GravityBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity

instance.GravityBeginEdit()
```

### C#

```csharp
void GravityBeginEdit()
```

### C++/CLI

```cpp
void GravityBeginEdit();
```

## VBA Syntax

See [CWGravity::GravityBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGravity~GravityBeginEdit.html).

## Remarks

To start editing gravity, you must call this method. You must call [ICWGravity::GravityEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWGravity~GravityEndEdit.html) to end editing gravity. Changes are not applied unless you call both methods.

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
