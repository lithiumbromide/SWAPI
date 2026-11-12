---
title: "RemoteLoadBeginEdit Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "RemoteLoadBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~RemoteLoadBeginEdit.html"
---

# RemoteLoadBeginEdit Method (ICWRemoteLoad)

Starts editing remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoteLoadBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad

instance.RemoteLoadBeginEdit()
```

### C#

```csharp
void RemoteLoadBeginEdit()
```

### C++/CLI

```cpp
void RemoteLoadBeginEdit();
```

## VBA Syntax

See [CWRemoteLoad::RemoteLoadBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~RemoteLoadBeginEdit.html).

## Examples

[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)

## Remarks

To start editing a remote load, you must call this method. You must call [ICWRemoteLoad::RemoteLoadEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRemoteLoad~RemoteLoadEndEdit.html) to end editing a remote load. Changes are not applied unless you call both methods.

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
