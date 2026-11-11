---
title: "InsertEmbeddedObjectFromFile Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertEmbeddedObjectFromFile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertEmbeddedObjectFromFile.html"
---

# InsertEmbeddedObjectFromFile Method (ISketchManager)

Adds an embedded object to the document based on the specified file.

## Syntax

### Visual Basic

```vb
Function InsertEmbeddedObjectFromFile( _
   ByVal FilePath As System.String, _
   ByVal Link As System.Boolean, _
   ByVal DisplayAsIcon As System.Boolean _
) As EmbeddedObject
```

### C#

```csharp
EmbeddedObject InsertEmbeddedObjectFromFile(
   System.string FilePath,
   System.bool Link,
   System.bool DisplayAsIcon
)
```

### JScript

```
function InsertEmbeddedObjectFromFile(
   FilePath : System.String,
   Link : System.boolean,
   DisplayAsIcon : System.boolean
) : EmbeddedObject;
```

### Managed Extensions for C++

```
EmbeddedObject* InsertEmbeddedObjectFromFile(
   System.string* FilePath,
   System.bool Link,
   System.bool DisplayAsIcon
)
```

### C++/CLI

```cpp
EmbeddedObject^ InsertEmbeddedObjectFromFile(
   System.String^ FilePath,
   System.bool Link,
   System.bool DisplayAsIcon
)
```

### Parameters

- `FilePath`: Path and file name of the embedded object to insert
- `Link`: True to insert a picture of the original file into the drawing, false to insert the contents of the file into the drawing (see **Remarks**)
- `DisplayAsIcon`: True to display the application icon in the drawing, false to display it in the data

### Return Value

[IEmbeddedObject](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)

## Examples

[Insert Embedded Object (JavaScript)](Insert_Embedded_Object_Example_JS.htm)
[Insert Embedded Object (VB.NET)](Insert_Embedded_Object_Example_VBNET.htm)
[Insert Embedded Object (C#)](Insert_Embedded_Object_Example_CSharp.htm)
[Insert Embedded Object (VBA)](Insert_Embedded_Object_Example_VBA.htm)

## Remarks

There are two ways to insert data from files:

- Linked object. Specify Link = true to insert a picture of the file into the drawing. When you edit a linked object, the source file changes. When you edit the source file, the linked object changes.
- Embedded object. Specify Link = false to insert the contents of the file into the drawing so that you may activate it using the source application that created it. Changes you make to the data in the embedded object do not appear in the original file, and changes you make to the original file do not appear in the drawing.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight V1R1.4
