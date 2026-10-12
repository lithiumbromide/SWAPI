---
title: "RemoteLoadEndEdit Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "RemoteLoadEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~RemoteLoadEndEdit.html"
---

# RemoteLoadEndEdit Method (ICWRemoteLoad)

Stops editing remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoteLoadEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim value As System.Integer

value = instance.RemoteLoadEndEdit()
```

### C#

```csharp
System.int RemoteLoadEndEdit()
```

### C++/CLI

```cpp
System.int RemoteLoadEndEdit();
```

### Return Value

Error code as defined in [swsRemoteLoadEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRemoteLoadEndEditError_e.html)

## VBA Syntax

See [CWRemoteLoad::RemoteLoadEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~RemoteLoadEndEdit.html).

## Examples

[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)

## Remarks

You must call [ICWRemoteLoad::RemoteLoadBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRemoteLoad~RemoteLoadBeginEdit.html) to start editing a remote load. To end editing a remote load, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
