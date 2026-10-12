---
title: "ICWForce Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html"
---

# ICWForce Interface

Allows access to the force object used by structural studies.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWForce
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
```

### C#

```csharp
public interface ICWForce
```

### C++/CLI

```cpp
public interface class ICWForce
```

## VBA Syntax

See [CWForce](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce.html).

## Examples

[Apply Loads to Beam (C#)](Apply_Loads_to_Beam_Example_CSharp.htm)
[Apply Loads to Beam (VB.NET)](Apply_Loads_to_Beam_Example_VBNET.htm)
[Apply Loads to Beam (VBA)](Apply_Loads_to_Beam_Example_VB.htm)
[Apply Table-driven Load to Multiple Beams (C#)](Apply_Table-driven_Load_to_Multiple_Beams_Example_CSharp.htm)
[Apply Table-driven Load to Multiple Beams (VB.NET)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VBNET.htm)
[Apply Table-driven Load to Multiple Beams (VBA)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VB.htm)
[Add Nonuniform Force Distribution (VBA)](Add_Force_Example_VB.htm)
[Add Nonuniform Force Distribution (VB.NET)](Add_Force_Example_VBNET.htm)
[Add Nonuniform Force Distribution (C#)](Add_Force_Example_CSharp.htm)

## Remarks

You can define uniform or nonuniform force. Forces are not required for frequency studies, but they are used if defined.

## Accessors

[ICWLoadsAndRestraintsManager::AddForce3](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager~AddForce3.html)

## See Also

[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
