---
title: "SetDocumentStatus Method (IPDMDocManager)"
project: "SOLIDWORKS Toolbox Browser API"
interface: "IPDMDocManager"
member: "SetDocumentStatus"
kind: "method"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IPDMDocManager~SetDocumentStatus.html"
---

# SetDocumentStatus Method (IPDMDocManager)

Sets the status of the currently active PDM document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDocumentStatus( _
   ByVal status As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMDocManager
Dim status As System.Integer
Dim value As System.Boolean

value = instance.SetDocumentStatus(status)
```

### C#

```csharp
System.bool SetDocumentStatus(
   System.int status
)
```

### C++/CLI

```cpp
System.bool SetDocumentStatus(
   System.int status
)
```

### Parameters

- `status`: Document status as defined in [swPDMStatus_e](SOLIDWORKS.Interop.swbrowser~SOLIDWORKS.Interop.swbrowser.swPDMStatus_e.html)

### Return Value

True if the document status is set, false if not

## VBA Syntax

See [PDMDocManager::SetDocumentStatus](ms-its:toolboxapivb6.chm::/ToolboxBrowser~PDMDocManager~SetDocumentStatus.html).

## Remarks

Available only if you installed SOLIDWORKS Toolbox.

## See Also

[IPDMDocManager Interface](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IPDMDocManager.html)
[IPDMDocManager Members](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.IPDMDocManager_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
