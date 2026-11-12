---
title: "eDScene Class"
project: ""
interface: "eDScene"
member: ""
kind: "class"
source: "emodeltoolkit/eDScene/eDScene_Class.htm"
---

# eDScene Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

A scene can represent an eDrawings document (.eprt, .easm, or .edrw file) and contains:

- either one or more configurations or a single drawing.
- the methods to create bodies, textures, and the functionality to save the scene to disk as a .eprt, .easm, or .edrw file.

#### Header file code

```vb
class eDScene : eDObject
{
public:

eDOutcome CreateBody( const eDAppearance &appearance, eBody *& body ); //Creates a body

eDOutcome CreateConfiguration( const ECHAR *configname, const eDImage &thumbnail, eDConfiguration *& configuration ); //Creates a configuration

eDOutcome CreateDrawing( eDDrawing *& drawing ); //Creates a drawing

eDOutcome CreateTexture( const eDImageByRef &image, eDParameterizationType texturetype, BOOL blended, eDTexture *& texture ); //Creates a texture

eDOutcome CreateSerializer( eDSerializer *& serializer ); //Creates the eDSerializer object

};
```
