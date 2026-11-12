---
title: "IDropData Interface"
project: ""
interface: "IDropData"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData.html"
---

# IDropData Interface

Do not use. Allows access to QMIMEData that is transferred during drag and drop in DraftSight.

## Syntax

### Visual Basic

```vb
Public Interface IDropData
```

### C#

```csharp
public interface IDropData
```

### JScript

```
public interface IDropData
```

### Managed Extensions for C++

```
public __gc __interface IDropData
```

### C++/CLI

```cpp
public interface class IDropData
```

## Remarks

This interface does not work in 2021 SP0.

A single QMimeData object can store the same data in several different formats (MIME types). This interface provides methods and properties that allow you to easily access drag and drop data for these specific MIME types:

- "text/plain"
- "text/html"
- "text/uri-list"
- "image/*"
- "application/x-color"

Other byte array data (e.g., "text/csv") and custom MIME types (e.g., "application/x-qt-windows-mime; value="<custom type>"") can be stored, retrieved, and removed using:

[IDropData::GetData](Interop.dsAutomation~Interop.dsAutomation.IDropData~GetData.html)

[IDropData::SetData](Interop.dsAutomation~Interop.dsAutomation.IDropData~SetData.html)

[IDropData::RemoveFormat](Interop.dsAutomation~Interop.dsAutomation.IDropData~RemoveFormat.html)

Implement _IDocumentEvents_DropNotifyEventHandler to notify you when a specific [drop action](Interop.dsAutomation~Interop.dsAutomation.dsDropAction_e.html) has occurred. When the DropNotify event occurs, the delegate returns the drop data which you can explore using this interface.

This interface functions like **Qt 5.15 > Qt Core > C++ Classes > QMimeData Class**. See https://doc.qt.io/qt-5/qmimedata.html.

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[_IDocumentEvents_DropNotifyEventHandler](Interop.dsAutomation~Interop.dsAutomation._IDocumentEvents_DropNotifyEventHandler.html)

## Access Diagram

[DropData](DSObjectModel.pdf#DropData)

## See Also

[IDropData Members](Interop.dsAutomation~Interop.dsAutomation.IDropData_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
