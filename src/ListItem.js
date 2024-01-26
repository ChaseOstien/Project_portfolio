

export default function ListItem({ project }) {

    return (
        <div className="project">
            <h2>{project.projectName}</h2>
            <p className="techs">{project.projectDescription}</p>
            <a href={project.repoLink} className="links">Repo Link</a>
            {project.deployed ? <a href={project.deployed} className="links">View Deployed Application</a> : <h4>This project is not deployed!</h4>}
         </div>
    )
}
