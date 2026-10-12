---
title: "ICWLoadsAndRestraintsManager Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html"
---

# ICWLoadsAndRestraintsManager Interface

Allows access to managing [loads and restraints](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraints.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWLoadsAndRestraintsManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
```

### C#

```csharp
public interface ICWLoadsAndRestraintsManager
```

### C++/CLI

```cpp
public interface class ICWLoadsAndRestraintsManager
```

## VBA Syntax

See [CWLoadsAndRestraintsManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## Remarks

Define a different study for each set of loads and restraints that occur simultaneously.

- For structural studies (static, dynamic, buckling, frequency, and nonlinear), the following types are valid:

- For thermal studies, the following types are valid:

- For frequency studies, loads are not required but they are used if defined. If you solve frequency studies without specifying restraints, you will get six (6) additional rigid body modes.

## Accessors

[ICWStudy::LoadsAndRestraintsManager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudy~LoadsAndRestraintsManager.html)

## See Also

[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWLoadsAndRestraints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html)
