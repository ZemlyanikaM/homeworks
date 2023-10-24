package ru.geekbrains.lesson1.store3d.inmemorymodel;

import ru.geekbrains.lesson1.store3d.modelelements.Camera;
import ru.geekbrains.lesson1.store3d.modelelements.Flash;
import ru.geekbrains.lesson1.store3d.modelelements.PoligonalModel;
import ru.geekbrains.lesson1.store3d.modelelements.Scene;

import java.util.ArrayList;
import java.util.List;


public class ModelStore implements ModelChanger {
    //TODO: Доработать в рамках домашней работы
    private List<PoligonalModel> models;
    private List<Flash> flashes;
    private List<Camera> cameras;
    private List<Scene> scenes;
    private List<ModelChangedObserver> changeObservers = new ArrayList<>();

    public ModelStore() throws Exception {
        this.changeObservers = null;
        this.models = new ArrayList<>();
        this.scenes = new ArrayList<>();
        this.flashes = new ArrayList<>();
        this.cameras = new ArrayList<>();
        models.add(new PoligonalModel(null));
        flashes.add(new Flash());
        cameras.add(new Camera());
        scenes.add(new Scene(0, models, flashes, cameras));
    }

    public Scene GetScena(int id) {
        for (int i = 0; i < scenes.size(); i++) {
            if (scenes.get(i).id == id) {
                return scenes.get(i);
            }
        }
        return null;
    }

    /**
     * Нотифицирует о событии
     */
    @Override
    public void notifyChange() {
        for (ModelChangedObserver observer : changeObservers) {
            observer.applyUpdateModel();
        }
    }

    @Override
    public void registerModelChanger(ModelChangedObserver o) {
        changeObservers.add(o);
    }

    @Override
    public void removeModelChanger(ModelChangedObserver o) {
        changeObservers.remove(o);
    }
}
